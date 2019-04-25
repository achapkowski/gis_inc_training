u = gis.users.create(username="A" + uuid.uuid4().hex[:5], 
                     password="Am4ziNgPassw0Rd", 
                     firstname="FIRSTNAME", 
                     lastname="LASTNAME",
                     email="fakeemail@esri.com", 
                     role="org_publisher", 
                     user_type="creatorUT")