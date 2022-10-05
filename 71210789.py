class NodeMahasiswa:

    def __init__(self,nama,ipk,n=None,p=None):
        self._element = nama
        self._ipk = ipk
        self._next = n
        self._prev = p

    def getNama(self):
        return self._element

    def getIpk(self):
        return self._ipk

    def setNama(self,nama):
        self._element = nama

    def setIpk(self,ipk):
        self._ipk = ipk

class DLLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def addElementTail(self, nama, ipk):
        baru = NodeMahasiswa(nama, ipk)
        if self._tail == None:
            self._head = baru
            self._tail = baru
            self._head._next = None
            self._head._prev = None
            self._tail._next = None
            self._tail._prev = None
        else:
            self._tail._next = baru
            baru._prev = self._tail
            self._tail = baru
            self._tail._next = None
        self._size += 1
        print("\n data masuk ke tail \n")
    
    def deleteLast (self):
        if self.isEmpty() == False:
            d = None
            helper = self._head
            if (self._head._next != None):
                hapus = self._tail
                self._tail = self._tail._prev
                d = hapus._element
                self._tail._next = None
                del hapus
            else:
                d = self._tail._element
                self._head = None
                self._tail = None
            self._size -= 1
            print("\n Data terhapus \n")
        else:
            print("Kosong!")
        
    def printAllDescending(self):
        helper = self._tail
        while helper!= None:
            print('====Print Descending==== \n======================== \nNama :', helper._element, '\nIPK  :', helper._ipk, '\n========================')
            helper =  helper._prev
    
    def rataIpk(self):
        helper = self._head
        totalIpk = 0
        while(helper!=None):
            totalIpk += helper.getIpk()    
            helper = helper._next
        rataRata=round(totalIpk/self._size,2)
        print('=====Rata - rata IPK==== \nRata - rata: ', rataRata)

DLLNC = DLLNC()
DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementTail('Harris',3.6)
DLLNC.printAllDescending()
DLLNC.deleteLast()
DLLNC.printAllDescending()
DLLNC.rataIpk()