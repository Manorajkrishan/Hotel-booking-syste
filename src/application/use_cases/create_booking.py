from uuid import UUID
from ..domain.entities.guest import Guest
from ..domain.entities.room import Room
from ..domain.services.booking_service import BookingService
from ..interfaces.repository import IBookingRepository, IRoomRepository
from ..interfaces.payment_service import IPaymentService
from ..dtos.booking_dto import BookingCreateDTO, BookingDTO

class CreateBookingUseCase:
    def __init__(
        self,
        booking_repo: IBookingRepository,
        room_repo: IRoomRepository,
        payment_service: IPaymentService,
        booking_service: BookingService,
    ):
        self.booking_repo = booking_repo
        self.room_repo = room_repo
        self.payment_service = payment_service
        self.booking_service = booking_service

    async def execute(self, booking_dto: BookingCreateDTO) -> BookingDTO:
        guest = await self.booking_repo.get_guest(booking_dto.guest_id)
        room = await self.room_repo.get_room(booking_dto.room_id)
        booking = await self.booking_service.create_booking(
            guest, room, booking_dto.check_in, booking_dto.check_out, booking_dto.num_guests
        )
        payment = await self.payment_service.process_payment(booking.payment.amount)
        if payment.status != booking.payment.status.COMPLETED:
            raise ValueError("Payment failed")
        await self.booking_repo.save(booking)
        return BookingDTO.from_entity(booking)