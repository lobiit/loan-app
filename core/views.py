from django.shortcuts import render, redirect
from django.views import View
from core.forms import CustomerForm
from core.models import Customer


def home(request):
    return render(request, 'home.html')


class Index(View):
    def get(self, request):
        form = CustomerForm(request.GET)
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        print('Printing the form data...\n', form.data)

        if form.is_valid():
            print("Form is valid")
            try:
                obj = form.save(commit=False)

                cust_dict = form.data
                print('Printing the value of cust_dict = form.data...\n', cust_dict)

                principal = int(cust_dict['loan_amount'])
                print(type(principal), 'loan_amount: ', principal)
                tenure = int(cust_dict['number_of_years'])
                print(type(tenure), 'number of years: ', tenure)
                rate = int(cust_dict['interest_rate'])
                print(type(rate), 'Rate: ', rate)

                amount = principal * pow((1 + rate/100), tenure)
                amount = principal * pow((1 + rate / 100), tenure)
                print(type(amount), 'Amount: ', amount)
                emi = int(amount/(tenure*12))
                emi = int(amount / (tenure * 12))
                print(emi)

                obj.monthly_rate = emi
                # wtf do you wanna achieve by this
                # kuch bhi mat likh
                # cust = Customer.objects.all()
                # for customers in cust:
                #     print(customers.user)
                #     customers.rate = customers.rate / (12 * 100)
                #     customers.tol = customers.tol * 12
                #
                #     emi = (customers.amount * customers.rate * pow(1 + customers.rate, customers.tol)) / (
                #         pow(1 + customers.rate, customers.tol))

                obj.save()
                print(" was saved in the database")

                return redirect('/show/')
            except:
                print("The Emi did not save in the database")
            pass

        else:
            form = CustomerForm()
        return render(request, 'index.html', {'form': form})


class Show(View):

    def get(self, request):
        all_loan = Customer.objects.all()
        print(all_loan)
        print('Printing the loans ')
        for cust in all_loan:
            print(cust.monthly_rate)

        return render(request, "show.html", {'all_loan': all_loan})
