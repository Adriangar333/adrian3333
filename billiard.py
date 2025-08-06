import math
import argparse
from dataclasses import dataclass
from typing import List, Tuple

try:
    import pygame
except Exception:  # pragma: no cover - pygame not always available
    pygame = None


@dataclass
class Ball:
    x: float
    y: float
    vx: float
    vy: float
    radius: int
    color: Tuple[int, int, int]

    def move(self, dt: float) -> None:
        self.x += self.vx * dt
        self.y += self.vy * dt


class BilliardGame:
    """Simple and reasonably optimized billiard simulation."""

    WIDTH, HEIGHT = 800, 400

    def __init__(self) -> None:
        self.balls: List[Ball] = [
            Ball(100.0, 200.0, 120.0, -30.0, 10, (255, 255, 255)),
            Ball(400.0, 200.0, -60.0, 80.0, 10, (0, 255, 0)),
            Ball(500.0, 230.0, 40.0, -100.0, 10, (255, 0, 0)),
        ]

    def _wall_collisions(self, ball: Ball) -> None:
        if ball.x - ball.radius < 0:
            ball.x = ball.radius
            ball.vx = -ball.vx
        if ball.x + ball.radius > self.WIDTH:
            ball.x = self.WIDTH - ball.radius
            ball.vx = -ball.vx
        if ball.y - ball.radius < 0:
            ball.y = ball.radius
            ball.vy = -ball.vy
        if ball.y + ball.radius > self.HEIGHT:
            ball.y = self.HEIGHT - ball.radius
            ball.vy = -ball.vy

    def _ball_collisions(self) -> None:
        n = len(self.balls)
        for i in range(n):
            bi = self.balls[i]
            for j in range(i + 1, n):
                bj = self.balls[j]
                dx = bj.x - bi.x
                dy = bj.y - bi.y
                dist2 = dx * dx + dy * dy
                if dist2 <= (bi.radius + bj.radius) ** 2 and dist2 != 0:
                    dist = math.sqrt(dist2)
                    nx, ny = dx / dist, dy / dist
                    p = 2 * ((bi.vx - bj.vx) * nx + (bi.vy - bj.vy) * ny) / 2
                    bi.vx -= p * nx
                    bi.vy -= p * ny
                    bj.vx += p * nx
                    bj.vy += p * ny
                    # push balls apart to avoid sticking
                    overlap = (bi.radius + bj.radius) - dist
                    bi.x -= nx * overlap / 2
                    bi.y -= ny * overlap / 2
                    bj.x += nx * overlap / 2
                    bj.y += ny * overlap / 2

    def step(self, dt: float) -> None:
        for ball in self.balls:
            ball.move(dt)
            self._wall_collisions(ball)
        self._ball_collisions()

    # Pygame loop (optional)
    def run(self) -> None:  # pragma: no cover - requires pygame
        if not pygame:
            raise RuntimeError("pygame is not installed")
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.step(dt)
            screen.fill((0, 100, 0))
            for b in self.balls:
                pygame.draw.circle(screen, b.color, (int(b.x), int(b.y)), b.radius)
            pygame.display.flip()
        pygame.quit()

    def simulate(self, steps: int, dt: float) -> List[Tuple[float, float]]:
        for _ in range(steps):
            self.step(dt)
        return [(b.x, b.y) for b in self.balls]


def main() -> None:
    parser = argparse.ArgumentParser(description="Billiard game")
    parser.add_argument("--simulate", type=int, default=0, help="run headless simulation for N steps")
    args = parser.parse_args()
    game = BilliardGame()
    if args.simulate:
        positions = game.simulate(args.simulate, 0.016)
        for i, (x, y) in enumerate(positions, 1):
            print(f"Ball {i}: {x:.2f}, {y:.2f}")
    elif pygame:
        game.run()
    else:
        print("pygame not installed; run with --simulate to test physics")


if __name__ == "__main__":
    main()
