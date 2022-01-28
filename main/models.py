from django.db import models
from ecdsa import VerifyingKey, BadSignatureError
import rsa
# Create your models here.
class PrivateData(models.Model):
    data=models.CharField(max_length=10000)


class User(models.Model):
    username=models.CharField( max_length=100)
    data=models.ManyToManyField(PrivateData,related_name="user_data")
    public_key=models.CharField( max_length=10000)
    verifying_key=models.CharField( max_length=10000)

    def verify(self,signature):
        vk=VerifyingKey.from_string(self.verifying_key)
        try:
            vk.verify(signature,self.username)
            return True
        except BadSignatureError:
            return False

    def get_PublicKey(self):
        return rsa.PublicKey.load_pkcs1_openssl_pem(self.public_key)


