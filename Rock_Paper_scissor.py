import random

player1 = input("Select Rock, Paper, or Scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Player 2 selected: ", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print(" ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅| llılılı Computer Won  ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅| llılılı")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif player1 == player2:
    print("𓆝 𓆟 𓆞 𓆝 𓆟 𓆞 𓆝 Tie 𓆝 𓆟 𓆞 𓆝 𓆟 𓆞 𓆝")
else:
    print("🌷͙֒₊˚*ੈ♡⸝⸝🪐⋆𓍢🌷͙֒₊˚*ੈ♡⸝⸝🪐Congratulations You Won 𓍢ִ໋🌷͙֒₊˚*ੈ♡⸝⸝🪐⋆𓍢🌷͙֒₊˚*ੈ♡⸝⸝🪐")