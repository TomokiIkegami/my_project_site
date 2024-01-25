from django.shortcuts import render
from django.views import View
from .models import SampleDB

class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app_folder/top_page.html')
    # def post(self, request, *args, **kwargs):
    #     input_data = request.POST['input_data']
    #     result = SampleDB.objects.filter(sample1=input_data)
    #     result_sample1 = result[0].sample1
    #     result_sample2 = result[0].sample2
    #     context = {'result_sample1':result_sample1, 'result_sample2':result_sample2}
    #     return render(request, 'app_folder/page02.html',context=context,)
    def happy_rc_page(request):
        return render(request,'app_folder/happy_rc_driver.html')
    def speedometer_page(request):
        return render(request,'app_folder/rc_speedometer.html')
    def tire_sim_page(request):
        return render(request,'app_folder/tire_simulation.html')
    def rtk_daisha_page(request):
        return render(request,'app_folder/rtk_autonomous_car.html')
    def elefit_page(request):
        return render(request,'app_folder/elefit.html')
    def smart_agri_page(request):
        return render(request,'app_folder/smart_agri_device.html')
    def paper_f1_page(request):
        return render(request,'app_folder/paper_f1.html')
    
top_page  = SampleView.as_view()
happy_rc_driver  = SampleView.happy_rc_page
rc_speedometer  = SampleView.speedometer_page
tire_sim  = SampleView.tire_sim_page
rtk_autonomous_car = SampleView.rtk_daisha_page
elefit = SampleView.elefit_page
smart_agri_device = SampleView.smart_agri_page
paper_f1 = SampleView.paper_f1_page
