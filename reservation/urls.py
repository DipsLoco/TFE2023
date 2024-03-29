
from django import views
from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('',home, name="home"),
    path('addshow',addshow, name="addshow"),
    path('all_shows', allShows , name="allShows"),
    path('allcours', allCours , name="allCours"),
    path('show/<int:show_id>', displayShow , name="show_detail" ),
    path('updateShow/<int:show_id>', updateShow, name='updateShow'),
    path('deleteShow/<int:show_id>', deleteShow, name="deleteShow"), 

    path('artist', allArtists , name="allArtists"), 
    path('apropos', aPropos , name="aPropos"),  # Visuel a faire
    path('artist/<int:artist_id>',showArtist, name='showArtist'),  # a rendre plus jolie
    path('artist/create/', artistCreate, name='artistCreate'),  # a rendre plus jolie
    path('artist/<int:artist_id>/edit', editArtist , name='artist_edit'), # a rendre plus jolie
    path('artist/<int:artist_id>/delete', deleteArtist, name='deleteArtist'),  # a rendre plus jolie
    
    path('type/',  show_all_type , name='type_show'),
    path('type/<int:type_id>', showType, name='type_detail'),

    path('locality/', allLocality, name='locality_index'),
    path('locality/<int:locality_id>', showLocality, name='locality_show'),

    path('myaccount/', displayUserAccount, name='myaccount' ),

    path('search_shows/', search_shows, name='search_shows' ),


    path('representation/create', createRepresentation, name='createRepresentation'),
    path('representation/<int:show_id>/reserver', representationReserver , name='representationReserver'),
    path('representation/<int:representation_id>/user_reservation', representationUserReservation , name='representationUserReservation'),
    path('reservation/<int:pk>/update/', ReservationUpdateView.as_view(), name='update_reservation'),

    path('payment/', payment, name='payment'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session' ),
    path('panier/', ProductLandingPageView.as_view(), name= 'landing-page'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    
    #path('role/', views.role.index, name='role_index'),
    #path('role/<int:role_id>', views.role.show, name='role_show'),
    #path('location/', views.location.index, name='location_index'),
    #path('location/<int:location_id>', views.location.show, name='location_show'),
    #path('show/', views.show_detail.index, name='show_index'),
    #path('show/<int:show_id>', views.show_detail.show, name='show_show'),
    #path('representation/', views.representation.index, name='representation_index'),
    #path('representation/<int:representation_id>', views.representation.show, name='representation_show'),


]
