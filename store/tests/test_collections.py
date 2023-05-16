from rest_framework import status
from store.models import Collection
from model_bakery import baker
import pytest


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/',collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection:
    # @pytest.mark.skip
    def test_if_user_is_anonymous_return_401(self,create_collection,authenticate):
        response = create_collection({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
        
    def test_if_user_is_not_admin_return_403(self,create_collection,authenticate):
        #Arrange
        authenticate(is_staff=False)
        #Act
        response = create_collection({'title':'a'})
        #Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN
        

    def test_if_data_is_invalid_400(self,create_collection,authenticate):
        authenticate(is_staff=True)
        
        response =create_collection({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
    
    
    def test_if_data_is_valid_201(self,create_collection,authenticate):
        authenticate(is_staff=True)        
        
        response = create_collection({'title':'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self, api_client):
        #Arrange.
        collection = baker.make(Collection)
        #Act.
        response = api_client.get(f'/store/collections/{collection.id}/')
        #Assert.
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id']== collection.id
        assert response.data['title'] == collection.title


        '''
        api_client.post('/store/collections/',title='a') it will throw the error.
        Collection.objects.create(title='a') this will create the mess

        we can also create the relationships as:
        collection = bake.make(Collection)
        baker.make(Product,collection=collection,_quantity=10)
        '''

        '''
        we can also write last two assert statments.
        assert response.data == {
            'id':collection.id,
            'title':collection.title,
            'product_count':0
        }
        '''