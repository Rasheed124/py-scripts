<!-- Look Before You Leap (LBYL) --> #  not consider as the best because of multiple checks before handling error

if can_i_do_x():
    do_x()
else:
    handle_error()

<!-- E.g -->

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print(f"Error: file {file_path} does not exist!")


<!-- conditions why this would fails -->

The path could be of a directory instead of a file
The file could be owned by a different user than the one attempting the deletion
The file could have read-only permissions
The disk on which the file is stored could be mounted as a read-only volume
The file could be locked by another process, a common annoyance on Microsoft Windows



<!-- Easier to Ask Forgiveness than Permission (EAFP) -->  #It means you should perform the action, and deal with any errors afterwards.

try:
    do_x()
except SomeError:
    handle_error()


try:
    os.remove(file_path)
except OSError as error:
    print(f"Error deleting file: {error}")


Concept
<!-- Hold on to the thought of not catching exceptions as an error handling strategy. -->



<!-- ========================= ==   Python Error Handling in the Real World =============================== -->

<!-- New Errors vs. Bubbled-Up Errors -  from it origin concept-->

Your code found a problem and needs to generate an error. I'll call this type a "new error".
Your code received an error from a function it called. I'll call this one a "bubbled-up error".



<!-- Recoverable vs. Non-Recoverable Errors -->

Aside from the error being new or bubbled-up, you need to decide if it is recoverable or not.correct before continuing. 

For example, if a piece of code tries to delete a file and finds that the file does not exist, it's not a big deal, it can just ignore the error and continue.

on-recoverable

A non-recoverable error is an error that the code in question cannot correct, or in other words, an error that makes it impossible for the code at this level to continue running. As an example, consider a function that needs to read some data from the database, modify it and save it back. If the reading fails, the function has to abort early, since it cannot do the rest of the work.


<!-- Type 1: Handling New Recoverable Errors -->

def add_song_to_database(song):
    # ...
    if song.year is None:
        song.year = 'Unknown'
    # ...



<!-- Type 2: Handling Bubbled-Up Recoverable Errors -->


def add_song_to_database(song):
    # ...
    try:
        artist = get_artist_from_database(song.artist)
    except NotFound:
        artist = add_artist_to_database(song.artist)
    # ...



<!-- Type 3: Handling New Non-Recoverable Errors -->


def add_song_to_database(song):
    # ...
    if song.name is None:
        raise ValueError('The song must have a name')
    # ...


<!--======== Creating python  exception subclasses -->

class ValidationError(Exception):
    pass

# ...

def add_song_to_database(song):
    # ...
    if song.name is None:
        raise ValidationError('The song must have a name')
    # ...



<!-- Type 4: Handling Bubbled-Up Non-Recoverable Errors -->


def new_song():
    song = get_song_from_user()
    add_song_to_database(song)

<!-- Catching All Exceptions -->


def my_cli()
    # ...

if __name__ == '__main__':
    try:
        my_cli()
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)