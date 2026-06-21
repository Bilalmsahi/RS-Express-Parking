from django.urls import path
from .views import BookingListCreate, BookingRescheduleView, CancelBookingView, ManagerBookingList, ManagerBookingStatusUpdate, BookingDetailView, UserBookingsView, BookingUserCreateView, BookingUserStatusUpdateView

urlpatterns = [
    path('', BookingListCreate.as_view(), name='booking-list-create'),
    path('<int:pk>/reschedule/', BookingRescheduleView.as_view(), name='booking-reschedule'),
    path('<int:pk>/cancel/', CancelBookingView.as_view(), name='booking-cancel'),
    path('manager/all/', ManagerBookingList.as_view(), name='manager-booking-list'),
    path('manager/<int:pk>/status/', ManagerBookingStatusUpdate.as_view(), name='manager-booking-status'),
    path('user/<int:user_id>/', UserBookingsView.as_view(), name='user-bookings'),
    path('booking-user/', BookingUserCreateView.as_view(), name='booking-user-create'),
    path('booking-user/<int:pk>/status/', BookingUserStatusUpdateView.as_view(), name='booking-user-status-update'),
    # Keep this last: <str:booking_code> is a catch-all single segment and would
    # otherwise shadow the named single-segment routes above (e.g. booking-user/).
    path('<str:booking_code>/', BookingDetailView.as_view(), name='booking-detail'),
]
