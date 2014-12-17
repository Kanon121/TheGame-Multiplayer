import Globals as gb


"""
baddie = gb.Enemy(300, 300, 'mummy.png')
baddie2 = gb.Enemy(500, 500, 'mummy.png')
gb.entities.append(baddie)
gb.entities.append(baddie2)
"""



while gb.edit.editing:
    gb.edit.RunEditor()


while gb.playing:

    

    time_passed = gb.clock.tick(60)
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            gb.playing = False
            
        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_ESCAPE:
            gb.edit.Saving()
            
    key = gb.pygame.key.get_pressed()

    if key[gb.pygame.K_a]:
        gb.player.update("left")
    if key[gb.pygame.K_d]:
        gb.player.update("right")
    if key[gb.pygame.K_s]:
        gb.player.update("down")
    if key[gb.pygame.K_w]:
        gb.player.update("up")

    gb.maps.render()    

    

    gb.cam.update(False) 
    
    for ents in gb.entities:
        ents.render(gb.cam)
        ents.see()
     
    
    gb.player.render(gb.cam)
    gb.player.see(gb.maps.new_blocks)
    gb.player2.checkCollisions(gb.player2, "player")
    gb.player.objCollision()

    gb.projectiles.Update()
    
    gb.overlay.render()
    

    gb.pygame.display.flip()
    gb.window.RenderWindow('black')
    
