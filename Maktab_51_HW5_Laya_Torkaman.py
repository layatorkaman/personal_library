media_list = []


def easy_print(media_lst):
    max_str_len = max(len(x.authors) for x in media_lst)

    for i in media_lst:
        print(f"|title : {i.title}", ' ' * (max_str_len - len(i.title)), '|',
              f"authors : {i.authors}", ' ' * (max_str_len - len(i.authors)), '|',
              f"media : {i.__class__.__name__}", ' ' * 2, '|',
              f"pages : {i.pages}", ' ' * 2, '|',
              f"progress : {i.progress}", ' ' * 1, '|')


class Book:
    def __init__(self, title, authors, publish_year, pages, language, price, was_read=0, progress=0):
        self.title = title
        self.authors = authors
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.was_read = was_read
        self.progress = progress
        self.status = None

    def read(self, new_read):
        self.was_read += new_read
        self.progress = round((self.was_read / self.pages) * 100, 2)
        if self.was_read > self.pages:
            self.was_read = self.pages
            self.progress = 100
        return f"you have read {self.was_read} more pages from {self.title}" \
               f"There are{self.pages - self.was_read}  pages left"

    def get_status(self):
        if self.was_read == 0:
            self.status = "Unread"
        elif self.was_read == self.pages:
            self.status = "Finished"
        else:
            self.status = "Reading"
        return self.status

    def __str__(self):
        return f'{self.title},' \
               f' {self.authors},' \
               f' {self.publish_year},' \
               f' {self.pages}' \
               f' {self.language},' \
               f' {self.price},' \
               f' {self.was_read}'

    @staticmethod
    def get_info_book():
        title = input('title :')
        authors = input('author(s) :')
        publish_year = int(input('publish_year:'))
        pages = int(input('number of pages :'))
        language = input('language :')
        price = float(input('price :'))
        was_read = int(input('was_read :'))
        new_book = Book(title, authors, publish_year, pages, language, price, was_read)
        media_list.append(new_book)
        return media_list


class Magazine(Book):
    def __init__(self, title, authors, publish_year, pages, language, price, issue, was_read=0, progress=0):
        super().__init__(title, authors, publish_year, pages, language, price, issue)
        self.issue = issue
        self.was_read = was_read
        self.progress = progress

    def __str__(self):
        return f'{self.title},' \
               f' {self.authors},' \
               f' {self.publish_year},' \
               f' {self.pages}' \
               f' {self.language}, ' \
               f' {self.price}, ' \
               f'{self.issue}'

    @staticmethod
    def get_info_magazine():
        title = input('title :')
        authors = input('author(s) :')
        publish_year = int(input('publish_year:'))
        pages = int(input('number of pages :'))
        language = input('language :')
        price = float(input('price :'))
        was_read = int(input('was_read :'))
        issue = int(input('issue :'))
        new_magazine = Magazine(title, authors, publish_year, pages, language, price, was_read, issue)
        media_list.append(new_magazine)
        return media_list


class Podcast_episode(Book):
    def __init__(self, title, speaker, publish_year, time, language, price, was_listened=0, progress=0):
        super().__init__(title, speaker, publish_year, time, language, price)
        self.speaker = speaker
        self.time = time
        self.was_listened = was_listened
        self.progress = progress

    def listen(self, new_listen):
        self.was_listened += new_listen
        self.progress = round((self.was_listened / self.time) * 100, 2)
        if self.was_listened > self.time:
            self.was_listened = self.time
            self.progress = 100
        return f"you have read {self.was_listened} more time from {self.title}" \
               f"There are{self.time - self.was_listened}  time left"
        #
        # self.was_listened += new_listen
        # if self.was_listened > self.time:
        #     self.was_listened = self.time
        # return f"you have listened {self.was_listened} more time from {self.title}" \
        #        f"There are{self.time - self.was_listened}  time left"

    def get_status(self):
        if self.was_listened == 0:
            self.status = "UnListened"
        elif self.was_listened == self.time:
            self.status = "Finished"
        else:
            self.status = "listening"
        return self.status

    def __str__(self):
        return f'{self.title},' \
               f' {self.speaker},' \
               f' {self.publish_year},' \
               f' {self.time}' \
               f' {self.language},' \
               f' {self.price},' \
               f' {self.was_listened}' \
               f' {self.progress}'

    @staticmethod
    def get_info_podcast_episode():
        title = input('title :')
        speaker = input('speaker :')
        publish_year = int(input('publish_year:'))
        time = int(input('time :'))
        language = input('language :')
        price = float(input('price :'))
        new_podcast = Podcast_episode(title, speaker, publish_year, time, language, price)
        media_list.append(new_podcast)
        return media_list


class Audio_book(Podcast_episode):
    def __init__(self, title, speaker, author, publish_year, pages, time, book_language, audio_language,
                 price, was_listened=0, progress=0):
        super().__init__(title, speaker, publish_year, time, audio_language, price, was_listened=0, progress=0)
        self.author = author
        self.pages = pages
        self.book_language = book_language
        self.audio_language = audio_language
        self.was_listened = was_listened
        self.progress = progress

    def __str__(self):
        return f'{self.title},' \
               f' {self.speaker},' \
               f' {self.author},' \
               f' {self.publish_year},' \
               f' {self.pages}' \
               f' {self.book_language},' \
               f' {self.audio_language},' \
               f' {self.time},' \
               f' {self.price},' \
               f' {self.was_listened}' \
               f' {self.progress}'

    @staticmethod
    def get_info_audio_book():
        title = input('title :')
        speaker = input('speaker :')
        author = input('author :')
        publish_year = int(input('publish_year:'))
        pages = int(input('pages:'))
        book_language = input('book_language:')
        audio_language = input('audio_language:')
        time = int(input('time :'))
        price = float(input('price :'))
        new_audio = Audio_book(title, speaker, author, publish_year, pages, book_language, audio_language, time, price)
        media_list.append(new_audio)
        return media_list


book1 = Book('No Friend But the Mountains', 'BehrouzBoochani', 2018, 374, 'English', 30, 10)
book1.read(20)
book2 = Book('Symphony of dead', 'BehrouzBoochani', 2018, 374, 'English', 0, 126)
podcast1 = Podcast_episode('Ravaaq', 'Farzin Ranjbar', 2020, 50, 'persian', 0, 10)
podcast1.listen(2)
book3 = Book('No Friend But The Mountains', 'Behrouz Boochani', 2018, 374, 'English', 10, 12)
book4 = Book('Symphony Of Dead', 'Behrouz Boochani', 2018, 374, 'English', 126)
magazine = Magazine('Bukhara', '[Ali Dehbashi,Darioush Ashoori]', 2020, 768, 'Persian', 55, 140, 23)
audio_book = Audio_book('The Black Swan', 'Ali Bandari', 'Nassim Nicholas Taleb', 2020, 400, 62, 'English',
                        'Persian', 0, 10)
media_list.append(podcast1)
media_list.append(book1)
media_list.append(book3)
media_list.append(book2)
media_list.append(magazine)
media_list.append(audio_book)

while True:
    print(
        "*********************************************** wellcome to your bookshelf**********************************"
        "*******************")
    print("what do you do?")
    print("1.Add a Book or magazine or podcast or Audio book")
    print("2.show my bookshelf")
    print("3.Add read page or time listen")
    print("4.sort my bookshelf")
    print("5.Quit")
    select = int(input("enter a number:"))
    if select == 1:
        select2 = int(input("please select another one: 1.book 2.magazine 3.podcast 4.audio book: "))
        if select2 == 1:
            Book.get_info_book()
        elif select2 == 2:
            Magazine.get_info_magazine()
        elif select2 == 3:
            Podcast_episode.get_info_podcast_episode()
        elif select2 == 4:
            Audio_book.get_info_audio_book()
    elif select == 2:
        easy_print(media_list)

    elif select == 3:
        select3 = int(input("please select: 1.book 2.magazine 3.podcast 4.audio book"))
        if select3 == 1 or select3 == 2:
            page = int(input("how many pages was read?"))
            name = input("enter the title")
            for item in media_list:
                if item.title == name:
                    print(item.read(page))

        if select3 == 3 or select3 == 4:
            times = int(input("how long was listen?"))
            name = input("enter the title")
            for item in media_list:
                if item.title == name:
                    print(item.listen(times))

    elif select == 4:
        sorted_media = sorted(media_list, key=lambda x: x.__getattribute__('progress'), reverse=True)
        easy_print(sorted_media)

    elif select == 5:
        break
