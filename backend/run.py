import sys
sys.dont_write_bytecode = True

from app import app

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000)