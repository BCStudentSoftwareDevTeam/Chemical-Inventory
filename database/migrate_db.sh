pem init

#pem add app.models.[filename].[classname]
pem add application.models.buildingsModel.Buildings
pem add application.models.chemicalsModel.Chemicals
pem add application.models.containersModel.Containers
pem add application.models.floorsModel.Floors
pem add application.models.historiesModel.Histories
pem add application.models.roomsModel.Rooms
pem add application.models.storagesModel.Storages
pem add application.models.usersModel.Users

pem watch
pem migrate
