import SID
import media
rush = media.Movie("Rush","An inspiring story of two greatest rivals in the history of formula 1 racing",
                        "http://pencurimovie.cc/wp-content/uploads/2013/12/rush_ver8_xlg.jpg",
                        "https://www.youtube.com/watch?v=lzNbGH1oZJc&hd=1")
avatar = media.Movie("Avatar","A marine on an alien planet","http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","http://www.youtube.com/watch?v=-9ceBgWV8io")
#avatar.show_trailer()                        
school_of_rock = media.Movie("School of Rock","Storyline", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
saving_private_Ryan=media.Movie("Saving Private Ryan", "storyline",
                     "http://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                     "https://www.youtube.com/watch?v=zwhP5b4tD6g&hd=1")
forest = media.Movie("Forrest Gump","Story line", "http://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
          "https://www.youtube.com/watch?v=eYSnxZKTZzU&hd=1")
dark_knight = media.Movie("Dark Knight","storyline","http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
               "https://www.youtube.com/watch?v=yQ5U8suTUw0&hd=1")
argo=media.Movie("Argo","Storyline","http://upload.wikimedia.org/wikipedia/en/e/e1/Argo2012Poster.jpg",
                 "http://www.youtube.com/watch?v=xVuG27Ij3Bs&hd=1")
inception=media.Movie("Inception","Storyline","http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg","https://www.youtube.com/watch?v=8hP9D6kZseM&hd=1")
movies=[dark_knight,argo,rush,inception,avatar,school_of_rock, saving_private_Ryan, forest]
SID.open_movies_page(movies)
