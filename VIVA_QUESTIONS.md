# PYGAME VIVA QUESTIONS & ANSWERS

## Basic Pygame Functions

### 1. pygame.init() kya karta hai?

**Answer:** Pygame ke saare modules ko initialize karta hai. Har pygame program mein sabse pehle yeh call karna zaroori hai.

### 2. pygame.display.set_mode() kya karta hai?

**Answer:** Game window create karta hai. Isme (width, height) tuple pass karte hain.

```python
screen = pygame.display.set_mode((800, 600))  # 800x600 window
```

### 3. pygame.display.set_caption() kya karta hai?

**Answer:** Window ka title set karta hai jo top bar mein dikhta hai.

### 4. screen.fill() kya karta hai?

**Answer:** Puri screen ko ek color se fill kar deta hai. Background color set karne ke liye use hota hai.

```python
screen.fill((0, 0, 0))  # Black background
```

### 5. pygame.display.flip() aur pygame.display.update() mein farq?

**Answer:**

- **flip()**: Puri screen ko update karta hai (faster)
- **update()**: Specific part ya puri screen update kar sakta hai (flexible)
- Dono ek hi kaam karte hain agar puri screen update karni ho
- like agar puri screen update krna hua to dono me se koi bhi use kro, but agar koi ek part jaise gun ya ball ko har sec update krna hua to .update use kro..

### 6. clock.tick(FPS) kya karta hai?

**Answer:** Game ki speed control karta hai. FPS (Frames Per Second) set karta hai.

```python
clock.tick(60)  # 60 FPS pe game chalega
```

### 7. pygame.event.get() kya karta hai?

**Answer:** Saare events (mouse click, key press, window close) ko list mein return karta hai.

### 8. pygame.QUIT event kya hai?

**Answer:** Jab user window ka close button (X) press karta hai tab yeh event trigger hota hai.

### 9. pygame.KEYDOWN event kya hai?

**Answer:** Jab koi keyboard key press hoti hai tab yeh event trigger hota hai.

### 10. pygame.key.get_pressed() kya karta hai?

**Answer:** Currently pressed keys ki list return karta hai. Continuous movement ke liye use hota hai.

---

## Drawing Functions

### 11. pygame.draw.rect() kya karta hai?

**Answer:** Screen pe rectangle draw karta hai.

```python
pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
```

### 12. pygame.draw.circle() kya karta hai?

**Answer:** Screen pe circle draw karta hai.

```python
pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
```

### 13. pygame.Rect kya hai?

**Answer:** Rectangle object jo position aur size store karta hai. Collision detection ke liye useful.

```python
player = pygame.Rect(x, y, width, height)
```

### 14. colliderect() kya karta hai?

**Answer:** Do rectangles ka collision check karta hai. True return karta hai agar overlap ho.

```python
if bullet.colliderect(enemy):
    # Collision hua
```

---

## Game Loop Concepts

### 15. Game loop kya hota hai?

**Answer:** While loop jo continuously chalta rehta hai. Events handle karta hai, game state update karta hai, aur screen draw karta hai.

### 16. Event handling kyun zaroori hai?

**Answer:** User input (keyboard, mouse, window close) ko process karne ke liye zaroori hai.

### 17. FPS kyun set karte hain?

**Answer:** Game ki speed consistent rakne ke liye. Bina FPS ke game fast computers pe bahut tez chalega.

---

## Practical-Specific Questions

### 18. Snake game mein snake kaise move hoti hai?

**Answer:** dx aur dy variables se direction store karte hain. Arrow keys se direction change hoti hai. Har frame mein x aur y position update hoti hai.

### 19. Infinite scrolling kaise kaam karta hai?

**Answer:** Background image ko multiple times draw karte hain. Scroll variable se position shift karte hain. Jab ek image screen se bahar jati hai, wapas starting position pe aa jati hai.

### 20. Snowfall effect kaise banta hai?

**Answer:** Multiple snow particles (circles) ki list banate hain. Har frame mein unka y position increase karte hain (neeche move). Jab screen se bahar jaye to wapas top pe reset kar dete hain.

### 21. Camera shake effect kaise kaam karta hai?

**Answer:** World surface ko random offset (x, y) pe draw karte hain. Shake duration ke liye random offsets generate karte hain. Duration khatam hone pe offset 0 kar dete hain.

### 22. Bouncing ball mein bounce kaise hota hai?

**Answer:** Ball ki speed ko -1 se multiply kar dete hain jab wall ya paddle se collision ho. Speed ki direction reverse ho jati hai.

### 23. Shooting game mein bullet kaise move hoti hai?

**Answer:** Bullet ki y position ko decrease karte hain (upar move). Jab screen se bahar jaye to list se remove kar dete hain.

### 24. Collision detection kaise karte hain?

**Answer:** colliderect() function use karte hain. Do Rect objects check karte hain ki overlap ho rahe hain ya nahi.

---

## Color & Coordinates

### 25. RGB color format kya hai?

**Answer:** (Red, Green, Blue) tuple. Har value 0-255 ke beech hoti hai.

- (255, 0, 0) = Red
- (0, 255, 0) = Green
- (0, 0, 255) = Blue
- (255, 255, 255) = White
- (0, 0, 0) = Black

### 26. Screen coordinates kaise kaam karte hain?

**Answer:**

- (0, 0) top-left corner hai
- x right ki taraf badhta hai
- y neeche ki taraf badhta hai

---

## Common Mistakes

### 27. pygame.quit() kyun zaroori hai?

**Answer:** Pygame modules ko properly close karne ke liye. Memory leaks avoid karne ke liye.

### 28. List ko iterate karte waqt remove karne mein problem kya hai?

**Answer:** Direct list iterate karte waqt remove karne se errors aa sakte hain. Isliye list[:] (copy) use karte hain.

```python
for bullet in bullets[:]:  # Copy use karo
    bullets.remove(bullet)
```

### 29. Event loop kyun zaroori hai?

**Answer:** Bina event loop ke window "Not Responding" ho jati hai. OS ko batana padta hai ki program abhi bhi chal raha hai.

---

## Advanced Concepts

### 30. pygame.Surface kya hai?

**Answer:** Image ya drawing area jo screen pe draw ho sakta hai. World surface camera shake mein use hota hai.

### 31. screen.blit() kya karta hai?

**Answer:** Ek surface ko dusre surface pe draw karta hai.

```python
screen.blit(world, (offset_x, offset_y))
```

### 32. random.choice() kya karta hai?

**Answer:** List se random element select karta hai.

```python
direction = random.choice([-1, 1])  # -1 ya 1
```

### 33. random.randint() aur random.randrange() mein farq?

**Answer:**

- **randint(a, b)**: a se b tak (including b)
- **randrange(a, b)**: a se b tak (excluding b)

### 34. Font rendering kaise karte hain?

**Answer:**

```python
font = pygame.font.SysFont("Arial", 30)
text = font.render("Score: 10", True, (255, 255, 255))
screen.blit(text, (10, 10))
```

---

## Tips for Viva

1. **Confidence se bolo** - Agar pura answer nahi pata to bhi jo pata hai wo clearly bolo
2. **Code example do** - Agar ho sake to chota example dikha do
3. **Practical se relate karo** - "Mere P5 snowfall mein maine yeh use kiya tha"
4. **Basic concepts clear rakho** - pygame.init(), game loop, event handling
5. **Common functions yaad rakho** - fill(), flip(), draw.rect(), draw.circle()

---

## Quick Revision Checklist

✅ pygame.init() - Initialize modules
✅ set_mode() - Window create
✅ fill() - Background color
✅ flip()/update() - Screen refresh
✅ clock.tick() - FPS control
✅ event.get() - Events lena
✅ QUIT, KEYDOWN - Event types
✅ draw.rect(), draw.circle() - Drawing
✅ Rect - Rectangle object
✅ colliderect() - Collision check
✅ RGB colors - (R, G, B) format
✅ Game loop - while run loop
✅ Event handling - for event in events

**ALL THE BEST FOR YOUR VIVA! 🎯💯**
