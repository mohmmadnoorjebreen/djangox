from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack
# Create your tests here.

class SnackTest(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'mohammad', email = 'mohammad@gmail.com', password = '1234'
        )
        self.snake = Snack.objects.create(
            title = 'Butterfinger',
            purchaser = self.user,
            description = 'This is good'
        )
        
    def test_str(self):
        self.assertEqual(str(self.snake) , 'Butterfinger')    
        
    def test_snake_content(self):
        self.assertEqual(self.snake.title , 'Butterfinger')  
        self.assertEqual(self.snake.description , 'This is good')  
        self.assertEqual(self.snake.purchaser.username , 'mohammad')  
        
    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))    
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Butterfinger')
        self.assertTemplateUsed(response,'snacks/snack_list.html')
        
    def test_snack_detail_view(self):
        response = self.client.get(reverse('snack_detail' , args='1')) 
        no_response = self.client.get('/54565/') 
        self.assertEqual(no_response.status_code,404)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Butterfinger')
        self.assertTemplateUsed(response,'snacks/snack_detail.html')     
             
 
    def test_create(self):
        response = self.client.post(
            reverse('snack_create'),
            {
                "title": "Twix",
                "description": "bad",
                "purchaser": self.user.id,
            }, 
            follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "description :bad")
        
        
    def test_snack_update_view(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "chips","description":"nice","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))    
        
    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        self.assertEqual(response.status_code, 200)    