import arcade

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Duel de Clics - Version Arcade"

# Constantes de jeu
PUSH_FORCE = 20    # Distance ajoutée à chaque clic
FRICTION = 0.2     # Vitesse à laquelle la barre revient au centre

class DuelGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Position de la séparation (au milieu au début)
        self.position_x = SCREEN_WIDTH // 2
        self.game_over = False
        self.winner = ""

        arcade.set_background_color(arcade.color.DARK_GRAY)

    def on_draw(self):
        """ Rendu de l'écran """
        self.clear()

        # 1. Dessiner la zone du Joueur 1 (Rouge)
        arcade.draw_lrtb_rectangle_filled(
            0, self.position_x, SCREEN_HEIGHT, 0, arcade.color.RED_ORANGE
        )

        # 2. Dessiner la zone du Joueur 2 (Bleu)
        arcade.draw_lrtb_rectangle_filled(
            self.position_x, SCREEN_WIDTH, SCREEN_HEIGHT, 0, arcade.color.ROYAL_BLUE
        )

        # 3. Dessiner la ligne de séparation
        arcade.draw_line(self.position_x, 0, self.position_x, SCREEN_HEIGHT, arcade.color.WHITE, 5)

        # 4. Afficher les scores/instructions
        arcade.draw_text("J1: Touche [A]", 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 18, bold=True)
        arcade.draw_text("J2: Touche [L]", SCREEN_WIDTH - 160, SCREEN_HEIGHT - 40, arcade.color.WHITE, 18, bold=True)

        # 5. Message de victoire
        if self.game_over:
            arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 500, 150, (0, 0, 0, 200))
            arcade.draw_text(self.winner, SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 10, 
                             arcade.color.WHITE, 24, align="center", anchor_x="center")
            arcade.draw_text("Appuyez sur ESPACE pour recommencer", SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40, 
                             arcade.color.LIGHT_GRAY, 14, align="center", anchor_x="center")

    def on_key_press(self, key, modifiers):
        """ Gestion des clics clavier """
        if not self.game_over:
            if key == arcade.key.A:
                self.position_x += PUSH_FORCE
            elif key == arcade.key.L:
                self.position_x -= PUSH_FORCE
        else:
            # Recommencer
            if key == arcade.key.SPACE:
                self.position_x = SCREEN_WIDTH // 2
                self.game_over = False

    def on_update(self, delta_time):
        """ Logique de mouvement automatique (Friction) """
        if not self.game_over:
            # La barre revient lentement vers le milieu
            if self.position_x > SCREEN_WIDTH // 2:
                self.position_x -= FRICTION
            elif self.position_x < SCREEN_WIDTH // 2:
                self.position_x += FRICTION

            # Vérifier les limites de l'écran (victoire)
            if self.position_x >= SCREEN_WIDTH:
                self.game_over = True
                self.winner = "VICTOIRE DU JOUEUR ROUGE !"
            elif self.position_x <= 0:
                self.game_over = True
                self.winner = "VICTOIRE DU JOUEUR BLEU !"

def main():
    game = DuelGame()
    arcade.run()

if __name__ == "__main__":
    main()