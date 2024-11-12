SYMBOLS: str = \
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


class CaesarsCipher:
    """
    Класс описывает шифр Цезаря
    """
    def decrypt(self,text_to_decrypt: str) -> str:
        """Расшифровка сообщения.

        Args:
            text_to_decrypt: Сообщение для расшифровки.

        Returns:
            Ключ и расшифрованное сообщение.
        """
        decrypted_result: list[str] = []
        for key in range(len(SYMBOLS)):
            text_decrypted: str = ''
            for symbol in text_to_decrypt:
                if symbol in SYMBOLS:
                    symbol_index: int = SYMBOLS.find(symbol)
                    new_index: int = symbol_index - key
                    if new_index < 0:
                        new_index += len(SYMBOLS)
                    text_decrypted += SYMBOLS[new_index]
                else:
                    text_decrypted += symbol
            decrypted_result.append(f'{key}: {text_decrypted}')
        return '\n'.join(decrypted_result)

    def encrypt(self, text_to_enrypt: str) -> str:
        """Шифровка сообщения.

        Args:
            text_to_enrypt: Сообщение для шифровки.

        Returns:
            Ключ и зашифрованное сообщение.
        """
        encrypted_result: list[str] = []
        for key in range(len(SYMBOLS)):
            text_encrypted: str = ''
            for symbol in text_to_enrypt:
                if symbol in SYMBOLS:
                    symbol_index: int = SYMBOLS.find(symbol)
                    new_index: int = symbol_index + key
                    if new_index >= len(SYMBOLS):
                        new_index -= len(SYMBOLS)
                    text_encrypted += SYMBOLS[new_index]
                else:
                    text_encrypted += symbol
            encrypted_result.append(f'{key}: {text_encrypted}')
        return '\n'.join(encrypted_result)


if __name__ == '__main__':
    text_decrypt: CaesarsCipher = CaesarsCipher()
    user_text_decrypt: str = input('Введите фразу для дешифрования: ')
    print(text_decrypt.decrypt(user_text_decrypt))
