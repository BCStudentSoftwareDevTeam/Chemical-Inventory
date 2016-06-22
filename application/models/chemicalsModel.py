from application.models.util import *

class Chemicals (Model):
  chemId          = PrimaryKeyField()
  ## General Information
  name            = CharField(unique = True)
  casNum          = CharField(null = False)
  primaryHazard   = CharField(null = False)
  formula         = CharField(null = False)
  concentration   = CharField()                   #This field can be left empty
  state           = CharField(null = False)
  structure       = CharField(null = False)       # Organic or Inorganic
  flashPoint      = FloatField(null = True)
  boilPoint       = FloatField(null = True)
  storageTemp     = FloatField(null = True)
  sdsLink         = CharField(null = True)
  description     = CharField(default = "")
  ## Hazards
  healthHazard    = CharField(null = False)       # Bool?
  flammable       = CharField(null = False)       # Bool?
  reactive        = CharField(null = False)       # Bool?
  other           = CharField(null = False)
  # Do we want to automatically decide which pictograms will show up? Or ask the user which pictograms a chemical should have?
  waterReactive   = BooleanField(default = False) # Water Reactive Pictogram
  hhPict          = BooleanField(default = False) # Health Hazard Pictogram # Couldn't we just check if the healthHazard field has been marked as True?
  flamePict       = BooleanField(default = False) # Flammmable Pictogram
  emPict          = BooleanField(default = False) # Explanation Mark
  gcPict          = BooleanField(default = False) # Gas Cylinder
  corrosivePict   = BooleanField(default = False) # Corrosive
  expPict         = BooleanField(default = False) # Explosive
  oxidizerPict    = BooleanField(default = False)
  oxidizerClass   = CharField(default = '4')      # Only if it is an oxidizer
  envPict         = BooleanField(default = False) # Environmental Hazard
  toxicPict       = BooleanField(default = False) # Acute Toxicity
  peroxideFormer  = BooleanField(default = False)
  pressureFormer  = BooleanField(default = False)

  class Meta:
    database = getDB("inventory")

