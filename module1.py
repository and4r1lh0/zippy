import random
import zipfile


def get_random_data(length):
    return "".join([chr(random.randrange(256)) for i in range(length)])


class MultiFile(object):
    def __init__(self, file_name, max_file_size):
        self.current_position = 0
        self.file_name = file_name
        self.max_file_size = max_file_size
        self.current_file = None        
        self.open_next_file()

    @property
    def current_file_no(self):
        return self.current_position / self.max_file_size

    @property
    def current_file_size(self):
        return self.current_position % self.max_file_size

    @property
    def current_file_capacity(self):
        return self.max_file_size - self.current_file_size

    def open_next_file(self):
        file_name = "%s.%03d" % (self.file_name, self.current_file_no + 1)
        print ("* Opening file '%s'..." % file_name)
        if self.current_file is not None:
            self.current_file.close()
        self.current_file = open(file_name, 'wb')

    def tell(self):
        print ("MultiFile::Tell -> %d" % self.current_position)
        return self.current_position

    def write(self, data):
        start, end = 0, len(data)
        print ("MultiFile::Write (%d bytes)" % len(data))
        while start < end:
            current_block_size = min(end - start, self.current_file_capacity)
            self.current_file.write(data[start:start+current_block_size])
            print ("* Wrote %d bytes." % current_block_size)
            start += current_block_size
            self.current_position += current_block_size
            if self.current_file_capacity == self.max_file_size:
                self.open_next_file()
            print ("* Capacity = %d" % self.current_file_capacity)

    def flush(self):
        print ("MultiFile::Flush")
        self.current_file.flush()


mfo = MultiFile('splitzip.zip', 2**1800)

zf = zipfile.ZipFile(mfo,  mode='w', compression=zipfile.ZIP_DEFLATED)


#for i in range(4):
#    filename = 'test%04d.txt' % i
#    print ("Adding file '%s'..." % filename)
#    zf.writestr(filename, get_random_data(2**17))

filename = 'test%04d.txt'
file = 'H:\WinPE10_8_Sergei_Strelec_x86_x64_2021.10.14_Russian.rar'
zf.writestr(filename, file)