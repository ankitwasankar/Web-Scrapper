from django.shortcuts import render
from . import utils


def home(request):
    """
    Display page with input textboxes and receive the inputs
    Send the inputs as parameter to spider to crawl the site
    """
    if request.method == 'GET':
        # if get method display html page
        context = {
            "msg": "",
        }
        return render(request, 'home.html', context)

    elif request.method == 'POST':
        # if post method call the spider with validated input
        msg = ""
        url = request.POST.get('url')
        depth = request.POST.get('depth')
        domain = True if request.POST.get('domain') else False
        # validate the inputs from user
        flag = utils.validate_params(url, depth, domain)
        # check validation
        if flag:
            # if validation returns true
            msg = "Spider started crawling webpages!"
            # call the start_spider method here--
            # code yet to add..
            context = {
                "msg": msg,
                "flag": "success",
            }
            return render(request, 'home.html', context)
        else:
            # if validation returns false
            msg = "Please input valid details!"
            context = {
                "msg": msg,
                "flag": "failed",
            }
            return render(request, 'home.html', context)
