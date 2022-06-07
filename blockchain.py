import datetime;
import hashlib;
import json;

class Blockchain:

    def __init__(self):
        self.chain = []
        self.createBlock()

    def createBlock(self, proof = 1, previousHash = 0):
        """ Creación de un nuevo bloque. 

            Arguments:
                - proof: Nounce del bloque actual. (proof != hash)
                - previous_hash: Hash del bloque previo.

            Returns: 
                - block: Nuevo bloque creado. 
        """
        block = {
            'index': len(self.chain)+1,
            'timestamp': str(datetime.datetime.now()),
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

    def proofOfWork(selfm, previous_proof):
        """ Protocolo de concenso Proof of Work (PoW).
    
            Arguments:
                - previous_proof: Nounce del bloque previo.

            Returns:
                - new_proof: Devolución del nuevo nounce obtenido con PoW. 
        """
        new_proof = 1
        check_proof = False
        while check_proof == False:
            hash = hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            if(hash[:4] == "0000"):
                check_proof = True
            else:
                new_proof+=1

        return new_proof

    def hash(self, block):
        """ Cálculo del hash de un bloque.
        
            Arguments:
                - block: Identifica a un bloque de la Blockchain.

            Returns:
                - hash_block: Devuelve el hash del bloque
        """

        encoded_block = json.dumps(block, sort_keys = True).encode()
        hash_block = hashlib.sha256(encoded_block).hexdigest()
        return hash_block

    def is_chain_valid(self, chain):
        """ Determina si la Blockchain es válida. 
        
        Arguments:
            - chain: Cadena de bloques que contiene toda la 
                    información de las transacciones.
        
        Returns:
            - True/False: Devuelve un booleano en función de la validez de la 
                        Blockchain. (True = Válida, False = Inválida) """

        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previousHash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True