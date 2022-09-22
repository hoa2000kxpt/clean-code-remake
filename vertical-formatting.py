## STILL CONVERTING!

from importlib.machinery import SourceFileLoader # import path
import os.path
import fs
# path = require('path');
# fs = require('fs');

class DiskStorage:
  def __init__(self, storageDirectory):
    self.storagePath = SourceFileLoader(storageDirectory);
    self.setupStorageDirectory()


  def setupStorageDirectory(self):
    if (!fs.existsSync(self.storagePath)):
      self.createStorageDirectory()
    else 
     print('Directory exists already.');


  def createStorageDirectory() {
    fs.mkdir(self.storagePath, self.handleOperationCompletion);
  }

  insertFileWithData(fileName, data) {
    if (!fs.existsSync(self.storagePath)) {
     print("The storage directory hasn't been created yet.");
      return;
    }
    const filePath = path.join(self.storagePath, fileName);
    fs.writeFile(filePath, data, self.handleOperationCompletion);
  }

  handleOperationCompletion(error) {
    if (error) {
      self.handleFileSystemError(error);
    } else {
     print('Operation completed.');
    }
  }

  handleFileSystemError(error) {
    if (error) {
     print('Something went wrong - the operation did not complete.');
     print(error);
    }
  }
}

const logStorage = new DiskStorage('logs');
const userStorage = new DiskStorage('users');

setTimeout(function () {
  logStorage.insertFileWithData('2020-10-1.txt', 'A first demo log entry.');
  logStorage.insertFileWithData('2020-10-2.txt', 'A second demo log entry.');
  userStorage.insertFileWithData('max.txt', 'Maximilian Schwarzmüller');
  userStorage.insertFileWithData('maria.txt', 'Maria Jones');
}, 1500);