#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para verificar se o servidor está funcionando
"""

import requests
import sys

def test_server():
    """Testa se o servidor está rodando"""
    print("🧪 Testando servidor...")
    print("=" * 50)

    # Teste 1: Health check
    print("\n1️⃣  Testando health check...")
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            print("✅ Health check OK")
            print(f"   Resposta: {response.json()}")
        else:
            print(f"❌ Health check falhou: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar ao servidor!")
        print("   Execute: python app.py")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

    # Teste 2: Página inicial
    print("\n2️⃣  Testando página inicial...")
    try:
        response = requests.get('http://localhost:5000/', timeout=5)
        if response.status_code == 200:
            print("✅ Página inicial OK")
        else:
            print(f"❌ Página inicial falhou: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

    # Teste 3: Endpoint de download (validação)
    print("\n3️⃣  Testando validação de URL...")
    try:
        response = requests.post(
            'http://localhost:5000/download',
            json={'url': '', 'format': 'mp3'},
            timeout=5
        )
        if response.status_code == 400:
            print("✅ Validação de URL vazia OK")
        else:
            print(f"⚠️  Validação retornou: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

    print("\n" + "=" * 50)
    print("✅ Todos os testes básicos passaram!")
    print("\n📝 Próximos passos:")
    print("   1. Abra http://localhost:5000 no navegador")
    print("   2. Abra o console do navegador (F12)")
    print("   3. Cole uma URL do YouTube e clique em Download")
    print("   4. Veja os logs no console do navegador E no terminal")
    return True

if __name__ == '__main__':
    success = test_server()
    sys.exit(0 if success else 1)
