from myblock import Blockchain

#Iniciar la cadena
blockchain = Blockchain()
#Obtener el bloque génesis
last_block = blockchain.last_block
#Crear una nueva transacción
proof = blockchain.proof_of_work(last_block)
origen = open('origen.txt').read()
blockchain.new_transaction({'content': origen,'items':10})
previous_hash = blockchain.hash(last_block)
#Crear un nuevo bloque con la transacción
block = blockchain.new_block(proof, previous_hash)

#Obtener el último bloque
last_block = blockchain.last_block
#Crear una nueva transaccion
destino = open('destino.txt').read()
proof = blockchain.proof_of_work(last_block)
blockchain.new_transaction({'content': destino,'items':10})
previous_hash = blockchain.hash(last_block)
#Crear un nuevo bloque con la transacción
block = blockchain.new_block(proof, previous_hash)
#Obtener la cadena
chain = blockchain.chain
#Modificar de manera fraudulenta la información
chain[1]['transactions'][0]['content'] = origen
#La cadena se rompe
print('Cadena rota' if not blockchain.valid_chain(chain) else 'cadena correcta')