from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# basically we are testing our model (checking all the fields in the model are working as 
# aspected or not).

class BlogTest(TestCase):

    @classmethod
    # Creating a User
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username = 'testuser1', 
            password = 'abc123',
        )
        testuser1.save()

        # creating a blog post
        test_post = Post.objects.create(
            author = testuser1, 
            title = 'Blog Title',
            body = 'Body Content'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'Body Content')
