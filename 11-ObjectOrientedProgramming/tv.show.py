# tv_show.py file
# main program
import tv

def main():
   # object creation
   tel = tv.TV()

   # object usage
   tel.show_status()
   tel.turn_on()
   tel.show_status()
   tel.turn_off()
   tel.show_status()
   
if __name__ == "__main__":
   main() 