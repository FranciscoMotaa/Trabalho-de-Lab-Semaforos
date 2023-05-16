import pygame 
  
pygame.init() 
white = (255, 255, 255) 
X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption('Sauron Todo Cego!') 
image = pygame.image.load(r'C:\Users\glcpo\OneDrive\Imagens\sauron_cego.jpg')
#imagem de um amigo meu todo cego 
while True : 
  
    
    
    display_surface.fill(white) 
  
    
    
    
    display_surface.blit(image, (0, 0)) 
  
    for event in pygame.event.get() : 
      
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
    pygame.display.update()  