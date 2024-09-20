class Amplifier:
    def on(self):
        print("Top-O-Line Amplifier on")
    
    def set_dvd(self, dvd):
        print(f"Top-O-Line Amplifier setting DVD player to {dvd}")
    
    def set_cd(self, cd):
        print(f"Top-O-Line Amplifier setting CD player to {cd}")
    
    def set_tuner(self, tuner):
        print(f"Top-O-Line Amplifier setting tuner to {tuner}")
    
    def set_surround_sound(self):
        print("Top-O-Line Amplifier surround sound on (5 speakers, 1 subwoofer)")
    
    def set_volume(self, volume):
        print(f"Top-O-Line Amplifier setting volume to {volume}")
    
    def off(self):
        print("Top-O-Line Amplifier off")

class Tuner:
    def on(self):
        print("Tuner on")
    
    def set_am(self):
        print("Tuner set to AM")
    
    def set_fm(self):
        print("Tuner set to FM")
    
    def set_frequency(self, frequency):
        print(f"Tuner frequency set to {frequency} MHz")
    
    def off(self):
        print("Tuner off")

class DvdPlayer:
    def __str__(self):
        return "Top-O-Line DVD Player"
    
    def on(self):
        print("Top-O-Line DVD Player on")
    
    def play(self, movie):
        print(f"Top-O-Line DVD Player playing '{movie}'")
    
    def stop(self):
        print("Top-O-Line DVD Player stopped")
    
    def eject(self):
        print("Top-O-Line DVD Player eject")
    
    def off(self):
        print("Top-O-Line DVD Player off")

class CdPlayer:
    def __str__(self):
        return "Top-O-Line CD Player"
    
    def on(self):
        print("Top-O-Line CD Player on")
    
    def play(self):
        print("Top-O-Line CD Player playing")
    
    def stop(self):
        print("Top-O-Line CD Player stopped")
    
    def eject(self):
        print("Top-O-Line CD Player eject")
    
    def off(self):
        print("Top-O-Line CD Player off")

class Projector:
    def on(self):
        print("Top-O-Line Projector on")
    
    def wide_screen_mode(self):
        print("Top-O-Line Projector in widescreen mode (16x9 aspect ratio)")
    
    def off(self):
        print("Top-O-Line Projector off")

class TheaterLights:
    def dim(self, level):
        print(f"Theater Ceiling Lights dimming to {level}%")
    
    def on(self):
        print("Theater Ceiling Lights on")

class Screen:
    def down(self):
        print("Theater Screen going down")
    
    def up(self):
        print("Theater Screen going up")

class PopcornPopper:
    def on(self):
        print("Popcorn Popper on")
    
    def pop(self):
        print("Popcorn Popper popping popcorn!")
    
    def off(self):
        print("Popcorn Popper off")


class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

if __name__ == "__main__":
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    cd = CdPlayer()
    projector = Projector()
    screen = Screen()
    lights = TheaterLights()
    popper = PopcornPopper()

    home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)

    home_theater.watch_movie("Raiders of the Lost Ark")
    home_theater.end_movie()
