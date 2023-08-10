package com.mirror.backend.common.utils;

import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.math.BigInteger;
import java.util.Base64;

@Component
public class IotEncryption {

    @Value("${iot.N}")
    public BigInteger N;

    @Value("${iot.E}")
    public BigInteger E;

    @Value("${iot.D}")
    public BigInteger D;

    public String encryption(String sentence, BigInteger n, BigInteger e) {
        byte[] bytes = sentence.getBytes();
        StringBuilder result = new StringBuilder();

        for (byte b : bytes) {
            BigInteger bi = BigInteger.valueOf(b & 0xFF); // Convert byte to positive BigInteger
            BigInteger encrypted = bi.modPow(e, n);
            char c = (char) encrypted.intValue();
            result.append(c);
        }

        // 암호화 된 문자열을 Base64로 인코딩하여 반환
        return Base64.getEncoder().encodeToString(result.toString().getBytes());
    }
    public String decryption(String encryptedBase64, BigInteger n, BigInteger d) {
        // Base64 디코딩 먼저 수행
        byte[] decodedBase64Bytes = Base64.getDecoder().decode(encryptedBase64);
        String decodedBase64String = new String(decodedBase64Bytes);

        StringBuilder decryptedResult = new StringBuilder();

        for (char c : decodedBase64String.toCharArray()) {
            BigInteger bi = BigInteger.valueOf(c & 0xFFFF); // Convert char to positive BigInteger
            BigInteger decrypted = bi.modPow(d, n);
            decryptedResult.append((char) decrypted.intValue());
        }

        return decryptedResult.toString();
    }

    public String encrytionText(String input){
        String output = encryption(input, N, E);
        return output;
    }

    public  String decryptionText(String input){
        String output = decryption(input, N, D);
        return output;
    }
}
