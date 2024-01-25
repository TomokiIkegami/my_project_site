from django.urls import path
from . import views

app_name = 'app_folder'
urlpatterns = [
    path('top_page/',views.top_page, name='top_page'),
    path('happy_rc_driver/',views.happy_rc_driver, name='happy_rc_driver'),
    path('rc_speedometer/',views.rc_speedometer, name='rc_speedometer'),
    path('tire_simulation/',views.tire_sim, name='tire_simulation'),
    path('rtk_autonomous_car/',views.rtk_autonomous_car, name='rtk_autonomous_car'),
    path('elefit/',views.elefit, name='elefit'),
    path('smart_agri_device/',views.smart_agri_device, name='smart_agri_device'),
    path('paper_f1/',views.paper_f1, name='paper_f1'),
]