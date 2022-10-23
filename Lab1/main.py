from AbstractFactory import *
from ObjPool import *
from Factory import *
from Builder import *

if __name__ == "__main__":
    
    print('============ Welcome to the Art Studio. ============\n')
    print("Here you can take a glance at the working processs of an artist!\n")

    
    ### Builder establishes the tools that are proposed for artist using(if he decises to work on a 
    # colored piece of work(involves the use of oilpainting and larger canvases) or a monochrome one(pencils are used along with smaller canvases) ###
    
    peisage = Colored()
    #portret = Monochrome()
    creation = Creation()

    creation.set_builder(peisage)
    p = creation.get_artsupply()
    p.art_tools()
    ##################
    
    #### Abstract Factory & here is used Singletone, Factory,  ObjPool  and Builder###

    factory = CreateArtFactory()
    
    ### Singletone is used in Factory that is used in Abstract Factory for establishing the painter that will work on a certain Art Type Piece ###
    p = Artist()
    artist = p.painter("Bob Ross")
    ##################
    
    ### Obj Pool is used in AbstractFactory for setting the nr of available canvases and easels. ###
    pool  = ToolPool(2)
    
    with PoolManager(pool) as c:
        a = c.tool('1')
    
    with PoolManager(pool) as e:
        b = e.tool('1')
    ##################
    
    ### Abstract Factory, here is used Factory for setting the art type of the artwork and builder for setting characteristics of objects ###
    ArtType = factory.get_artpiece_type()
    Canvas = factory.get_canvas()
    Easel = factory.get_easel()
    Tools = factory.get_tools()
    
    print(ArtType.get_type(artist))
    print(Canvas.take(a, peisage.get_canvas().size))
    print(Easel.get(b, peisage.get_easel().brand))
    print(Tools.get_material(peisage.get_tools().material))
    
    print("\n============ The artist is actively working on his artwork. ============\n")
    ##################
    
    
    
    

 
    

    