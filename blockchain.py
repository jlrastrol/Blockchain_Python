import datetime;
import hashlib;
import json;
from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok

class Blockchain:

    def __init__(self):
        self.chain = []
        self.createBlock()

    def createBlock(self, proof = 1, data = {}, previousHash = 0):
        """ Creación de un nuevo bloque. 

            Arguments:
                - proof: Nounce del bloque actual. (proof != hash)
                - data: Datos del bloque. (Transacciones)
                - previous_hash: Hash del bloque previo.

            Returns: 
                - block: Nuevo bloque creado. 
        """
        block = {
            'index': len(self.chain)+1,
            'timestamp': str(datetime.datetime.now()),
            'data': data,
            'proof': proof,
            'previousHash': previousHash
        }
        self.chain.append(block)
        return block

    def getPreviousBlock(self):
        """ Obtención del bloque previo de la Blockchain .
    
            Returns:
                - Obtención del último bloque de la Blockchain. 
        """
        return self.chain[-1]
