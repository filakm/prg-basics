# class definition
class Song:
   def __init__(self,performer,title,album,year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
      return f' {self.performer}\n {self.title}\n {self.album}\n {self.year}'
# object creation
song1 = Song('Queen', 'Bohemian Rhapsody', 'a night at the opera', 1975)
song2 = Song('Ed Sheeran', 'hearts dont break', 'divide', 2017)


## object usage
print(song1)
print(song2)