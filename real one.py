import flet as ft
import flet_audio as fta
import random

def main(page: ft.Page):
    page.title = "Song Quiz"
    songs = {
        "1980s": [
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Billie Jean.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Everybody Want To Rule The World.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Every Breath You Take.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Everywhere.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Like A Prayer.mp3"}
        ],
        "2000s": [
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Sweater Weather.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Last Friday Night.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Get Lucky.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Gangnam Style.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Danza Kuduro.mp3"}
        ],
        "2020s": [
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Blinding Lights.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Brooklyn.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Golden Hour.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Let The Light In.mp3"},
            {"src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Levitating.mp3"}
        ]
    }

    current_category = {"name": None, "song": None}

    audio_player = fta.Audio(
        src=r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\getlucky.mp3",
        autoplay=False,
        volume=1
    )
    page.overlay.append(audio_player)

    timer_text = ft.Text(value="Time remaining: 5", size=20)

    def countdown(seconds):
        if seconds >= 0:
            timer_text.value = f"Time remaining: {seconds}"
            page.update()
            if seconds > 0:
                page.after(1000, lambda: countdown(seconds - 1))
            else:
                audio_player.pause()

    def seek_rand(e):
        if current_category["song"]: 
            audio_player.pause()
            audio_player.seek(0)
            audio_player.resume()
            countdown(5)

            def stop_audio():
                audio_player.pause()
                audio_player.seek(0)
                page.update()

            page.after(5000, stop_audio)


    def rand_song(e):
        if current_category["name"]:
            song_dict = random.choice(songs[current_category["name"]])
            current_category["song"] = song_dict["src"]
            audio_player.src = current_category["song"]
            audio_player.play()
            page.update()

    def select_category(e):
        current_category["name"] = e.control.text
        rand_song(None)

    def pause(e):
        audio_player.pause()
        page.update()

    page.add(ft.Text("Welcome to the Song Quiz! To play, you must have great musical knowledge! Start by clicking on your preffered category, then click 'Play Song'. After clicking, listen to the song. Once you have the answer, type it in the text box and click 'Check Answer'. Now, you can guess the song playing and enjoy!"))

    category_buttons = [ft.ElevatedButton(text=category, on_click=select_category) for category in songs.keys()]

    for button in category_buttons:
        page.add(button)

    user_guess = ft.TextField(label="Write your guess here")
    result_text = ft.Text("")

    def check_guess(e):
        if current_category["name"] and user_guess.value.lower() in current_category["song"].lower():
            result_text.value = "Correct, nice work!"
        else:
            result_text.value = "Wrong answer, try again!"
        page.update()

    pause_Btn = ft.ElevatedButton(text="Pause", on_click=pause)
    check_Btn = ft.ElevatedButton("Check Answer", on_click=check_guess)
    next_Btn = ft.ElevatedButton("Next Song", on_click=rand_song)
    play_Btn = ft.ElevatedButton("Play Song", on_click=seek_rand)

    page.add(
        user_guess,
        check_Btn,
        pause_Btn,
        next_Btn,
        play_Btn,
        result_text
    )

ft.app(target=main)