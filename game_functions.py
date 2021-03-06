import sys
import pygame
from lasers import Laser
from alien import Alien
from time import sleep


def check_keydown_events(event, game_settings, screen, ship, lasers):
    if event.key == pygame.K_RIGHT:  # If users click left arrow then ship moves left
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # If users click right arrow then ship moves right
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # If users click space then laser will be fired
        fire_laser(game_settings, screen, ship, lasers)
    elif event.key == pygame.K_q:  # If users click Q then the game will close
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(game_settings, screen, stats, sb, play_button, ship, aliens, lasers):
    for event in pygame.event.get():
        # For loop that watches for keyboard and mouse events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, lasers)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, sb, play_button, ship, aliens, lasers, mouse_x, mouse_y)


# Starts a new game when the player clicks play
def check_play_button(game_settings, screen, stats, sb, play_button, ship, aliens, lasers, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        game_settings.initialize_dynamic_settings()  # Reset the game settings
        pygame.mouse.set_visible(False)  # This will hide the mouse cursor
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_score()
        sb.prep_level()
        #sb.prep_ships_left()

        aliens.empty()
        lasers.empty()
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(game_settings, screen, stats, sb, ship, aliens, lasers, play_button):
    # Continually updates the background color in the while loop.
    screen.fill(game_settings.bg_color);
    # Displays the score info
    sb.show_score()

    for laser in lasers.sprites():
        laser.draw_laser()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    # This is basically an illusion that shows elements moving smoothly.
    pygame.display.flip()


def fire_laser(game_settings, screen, ship, lasers):
    if len(lasers) < game_settings.lasers_allowed:
        new_laser = Laser(game_settings, screen, ship)
        lasers.add(new_laser)


def update_lasers(game_settings, screen, stats, sb, ship, aliens, lasers):
    lasers.update()
    for laser in lasers.copy():
        if laser.rect.bottom <= 0:
            lasers.remove(laser)
    check_laser_alien_collisions(game_settings, screen, stats, sb, ship, aliens, lasers)


def check_laser_alien_collisions(game_settings, screen, stats, sb, ship, aliens, lasers):
    collisions = pygame.sprite.groupcollide(lasers, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_point_worth * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        lasers.empty()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, ship, aliens)

        # Increases level part, only if the entire fleet is destroyed
        stats.level += 1
        sb.prep_level()




def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_settings, ship_height, alien_height):
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    for row_num in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_num)


def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def update_aliens(game_settings, stats, screen, sb, ship, aliens, lasers):
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, sb, ship, aliens, lasers)
    test_aliens_bottom(game_settings, stats, screen, sb, ship, aliens, lasers)


def ship_hit(game_settings, stats, screen, sb, ship, aliens, lasers):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # Decrement ships left to play with
        #sb.prep_ships_left()

        # Empties the list of aliens and lasers
        aliens.empty()
        lasers.empty()

        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def test_aliens_bottom(game_settings, stats, screen, sb, ship, aliens, lasers):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, sb, ship, aliens, lasers)
            break
