from django.shortcuts import render, get_object_or_404
from .forms import UserForm, UserProfileInfoForm, UpdateProfileForm
from django.views.generic import DetailView,UpdateView,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo, User
import random

# Create your views here.

@login_required
def user_logout(request):
    #del request.session['user_id']
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

class Aboutpageview(TemplateView):
    template_name='accounts/about.html';


class Intropageview(TemplateView):
    template_name='accounts/intro.html';

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

        if registered:
            return HttpResponseRedirect(reverse('user_login'))

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.profile.pk

                return HttpResponseRedirect(reverse('predict:predict', kwargs={'pk': user.profile.pk}))
            else:
                return HttpResponse("Account not active")
        else:
            print("Tried login and failed")
            print("username: {} and password: {}".format(username, password))
            # return HttpResponse("Invalid login details supplied!")
            return render(request, 'accounts/invalidLogin.html', {})

    else:
        return render(request, 'accounts/login.html', {})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = UserProfileInfo
    template_name = 'accounts/profileview.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('user_id'):
            u_id = self.request.session['user_id']
            context = super(ProfileDetailView, self).get_context_data(**kwargs)
            context['user_id'] = u_id

        return context

name = ['Name: '
        'Name: Dr. A K Bardhan',
        'Name: Dr. Siddhartha Mani',
        'Name: Dr. Jayanta Saha',
        'Name: Dr. Indranil Dutta',
        'Name: Dr. Aftab Khan',
        'Name: Dr. Parijat Deb Choudhury',
        'Name: Dr Soumitra Kumar',
        'Name: Dr. Arvind Kumar',
        'Name: Dr Suchit Majumdar',
        'Name: Dr Kunal Sarkar',
        'Name: Dr. Amal Kumar Khan',
        'Name: Dr Arindam Pande',
        'Name: Dr Rabin Chakraborty',
        'Name: Dr K S Poddar MD DM',
        'Name: Dr. Arup Dasbiswas',
        'Name: Dr. Debashis Ghosh',
        'Name: Dr Prakash Chandra Mandal',
        'Name: Dr Rajkumar Dutta',
        'Name: Dr. Sankha Subhra Das',
        'Name: Dr Anil Mishra',
        'Name: Dr. Indranil Dutta',
        'Name: Dr. Sunando Adhikari',
        'Name: Dr Achyut Sarkar',
        'Name: Dr Sunil Lhila',
        'Name: Dr. Dhiman Kahali',
        'Name: Dr Dilip Kumar',
        'Name: Dr Sankar Kumar Chatterjee']

rating = ["Rating: "
        "Rating: 4.5",
         "Rating: 4.7",
         "Rating: 2.5",
         "Rating: 4.5",
         "Rating: 4.8",
         "Rating: 5",
         "Rating: 4.5",
         "Rating: 4.2",
         "Rating: 4.2",
         "Rating: 3.8",
         "Rating: 3.4",
         "Rating: 4.9",
         "Rating: 3.2",
         "Rating: 4.4",
         "Rating: 2.9",
         "Rating: 3.7",
         "Rating: 4.2",
         "Rating: 4.8",
         "Rating: 5",
         "Rating: 3.2",
         "Rating: 4.5",
         "Rating: 5",
         "Rating: 4.3",
         "Rating: 4.7",
         "Rating: 4.5",
         "Rating: 4.7",
         "Rating: 4.8",
         ]


contact = ["Contact No: ",
            "Contact No: 1860 500 1066",
          "Contact No: 098318 94526",
          "Contact No: 1860 500 1066",
          "Contact No: 1860 500 4916",
          "Contact No: 1860 500 1066",
          "Contact No: 033 4058 5544",
          "Contact No: 082320 32519",
          "Contact No: 1860 500 4916",
          "Contact No: 090518 83987",
          "Contact No: 098316 26553",
          "Contact No: 033 2563 1855",
          "Contact No: 090380 64946",
          "Contact No: 098363 70453",
          "Contact No: 094330 89596",
          "Contact No: 070023 18894",
          "Contact No: 1860 500 1066",
          "Contact No: 098317 41032",
          "Contact No: 033 2564 7944",
          "Contact No: 033 6540 2963",
          "Contact No: 033 4450 4145",
          "Contact No: 1860 500 4916",
          "Contact No: 1860 500 1066",
          "Contact No: 033 2223 5181",
          "Contact No: 033 7122 2222",
          "Contact No: 033 3040 3355",
          "Contact No: 092300 90526",
          "Contact No: 098300 33677",
          ]


address = ["Address: ",
            "Address: Apollo Gleneagles Hospital Limited, 58, Canal Circular Rd, Kadapara, Phool Bagan, Kankurgachi, Kolkata, West Bengal 700054",
          "Address: 124, Eastern Metropolitan Bypass, Mukundapur Market, Stadium Colony, Mukundapur, Kolkata, West Bengal 700099",
          "Address: 33-42, Ground Floor, The Galleria - Dlf, Plot No BG-8, Apollo Clinic, Action Area 1B, Newtown, Kolkata, West Bengal 700156",
          "Address: P 72, Prince Anwar Shah Road, Opp. South City Mall, CIT Scheme 114 B Apollo Clinic, Prince Anwar Shah Rd, Kolkata, West Bengal 700045",
          "Address: Apollo Gleneagles Hospital Limited, 58, Canal Circular Rd, Kadapara, Phool Bagan, Kankurgachi, Kolkata, West Bengal 700075",
          "Address: 1412, Medithics Clinic, near R. N. Tagore Hospital, Mukundapur, Kolkata, West Bengal 700099",
          "Address: P-273, Bangur Avenue, Block A, Ballygunge, Kolkata, West Bengal 700055",
          "Address: P 72, Prince Anwar Shah Road, Opp. South City Mall, CIT Scheme 114 B Apollo Clinic, Prince Anwar Shah Rd, Kolkata, West Bengal 700045",
          "Address: 58, Canal Circular Road apollo hospital, Kadapara, Phool Bagan, Kolkata, West Bengal 700054",
          "Address: Attached with Medica Hospital, 42/1A, Harish Mukherjee Rd, Bhowanipore, Kolkata, West Bengal 700025",
          "Address: 11 No, Bus Stop, 29, Barrackpore Trunk Rd, Manasbag, Belghoria, Kolkata, West Bengal 700056",
          "Address: 48/2b, Barrackpore Trunk Rd, South Sinthee, University Of Calcutta, Sinthee, Kolkata, West Bengal 700050",
          "Address: BE-407, BE Block, Sector 1, Bidhannagar, Kolkata, West Bengal 700064",
          "Address: 52, Dr SP Mukherjee Rd, Mahendra Colony, Cantonment, Rajbari, Dum Dum, Kolkata, West Bengal 700028",
          "Address: C.I.T. Road Scheme, Paddapukur, Entally, Kolkata, West Bengal 700014",
          "Address: Apollo Gleneagles Hospital Limited, 58, Canal Circular Rd, Kadapara, Phool Bagan, Kankurgachi, Kolkata, West Bengal 700054",
          "Address: 64/1/16A, Khudiram Bose Sarani, Kolkata, West Bengal 700037",
          "Address: 6, M M Feeder Road, Ariadaha P O, Kolkata, West Bengal 700057",
          "Address: Apollo Gleneagles Hospital Limited, 58, Canal Circular Rd, Kadapara, Phool Bagan, Kankurgachi, Kolkata, West Bengal 700054",
          "Address: Alipore, Kolkata, West Bengal 700027",
          "Address: P 72, Prince Anwar Shah Road, Opp. South City Mall, CIT Scheme 114 B Apollo Clinic, Prince Anwar Shah Rd, Kolkata, West Bengal 700045",
          "Address: 33-42, Ground Floor, The Galleria - Dlf, Plot No BG-8, Apollo Clinic, Action Area 1B, Newtown, Kolkata, West Bengal 700156",
          "Address: IPGMER & SSKM Hospital, 244 A, J C Bose Road, Kolkata, West Bengal 700020",
          "Address: 124, Mukundapur, E M Bypass, Kolkata, West Bengal 700099",
          "Address: 1, 1, National Library Ave, Alipore, Kolkata, West Bengal 700027",
          "Address: Medica Superspecialty Hospital, 127, Eastern Metropolitan Bypass, Nitai Nagar, Mukundapur, Kolkata, West Bengal 700099",
          "Address: Blind School, 19/2, Dr Akshay Kumar Paul Rd, Opp:, Behala, Kolkata, West Bengal 700034"
          ]


def predict_recomm(request):
        value1 =random.randint(1, 10)
        value2 =random.randint(11, 20)
        value3 =random.randint(21, 25)
        value4 =random.randint(1, 26)


        # for num in range(100):
        names1 = name[value1]
        ratings1 = rating[value1]
        contacts1 = contact[value1]
        addresses1 = address[value1]



        names2 = name[value2]
        ratings2 = rating[value2]
        contacts2 = contact[value2]
        addresses2 = address[value2]



        names3 = name[value3]
        ratings3 = rating[value3]
        contacts3 = contact[value3]
        addresses3 = address[value3]


        names4 = name[value4]
        ratings4 = rating[value4]
        contacts4 = contact[value4]
        addresses4 = address[value4]


        return render(request, 'accounts/recommendation.html', context={'doctor11': names1, 'doctor12': ratings1, 'doctor13': contacts1, 'doctor14': addresses1,
                                                                        'doctor21': names2, 'doctor22': ratings2, 'doctor23': contacts2, 'doctor24': addresses2,
                                                                        'doctor31': names3, 'doctor32': ratings3, 'doctor33': contacts3, 'doctor34': addresses3,
                                                                        'doctor41': names4, 'doctor42': ratings4, 'doctor43': contacts4, 'doctor44': addresses4})
