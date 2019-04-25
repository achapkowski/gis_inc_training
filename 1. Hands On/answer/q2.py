# Find the States Layer
results = [item for item in \
         gis.content.search("""generalized and states and USA AND owner:esri_dm""", item_type="Feature Layer", max_items=5) \
         if item.title == "USA States (Generalized)"]
states = results[0]
items.append(states)
# Find the Rivers and Streams
results = gis.content.search("""title:'USA Rivers and Streams' AND owner:esri""", item_type="Feature Layer", max_items=5)
results = [item for item in results if item.title == 'USA Rivers and Streams']
items += results
# Find the Cities
results = gis.content.search("""USA Major Cities AND owner:esri_dm""", item_type="Feature Layer", max_items=5)
items += results
items
