def sortPost(data, model):
  
  """
    Takes a dictionary and a model to replace empty strings with None.
    It also splits post data into two variable model_data and extra_data.
    Model data only has feilds present in the model, extra has all extra data.
    Credit: Jesson Soto
  """
  model_data = dict()
  extra_data = dict()
  for key in iter(data):
    if data[key] == "":
      if hasattr(model, key):
        if getattr(model, key).null == True:
          model_data[key] = None
        else:
          model_data[key] = data[key]
      else:
        extra_data[key] = data[key]
      
    elif hasattr(model, key):
      model_data[key] = data[key]
    else:
     extra_data[key] = data[key]
  return (model_data, extra_data)