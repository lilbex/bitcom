from django.forms import ModelForm
from .models import announced_pu_results
import socket   




def get_ip_address():
  hostname = socket.gethostname()    
  IPAddr = socket.gethostbyname(hostname)
  return IPAddr    


# class PollingUnitForm(ModelForm):
#   user_ip_address = get_ip_address()
#   class Meta:
#       model = announced_pu_results
#       fields = ['polling_unit_uniqueid','party_abbreviation', 'party_score', 'entered_by_user','date_entered','user_ip_address']
