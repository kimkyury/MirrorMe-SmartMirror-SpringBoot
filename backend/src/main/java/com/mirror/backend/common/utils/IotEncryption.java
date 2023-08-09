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

    @Value("${iot.PNA}")
    public BigInteger E;

    @Value("${iot.PNB}")
    public BigInteger D;

    public  String encryption(String sentence, BigInteger  n, BigInteger  e) {

        byte[] bytes = Base64.getEncoder().encode(sentence.getBytes());
        StringBuilder result = new StringBuilder();
        for (byte b : bytes) {
            BigInteger bi = BigInteger.valueOf(b & 0xFF); // Convert byte to positive BigInteger
            BigInteger encrypted = bi.modPow(e, n);
            char c = (char) encrypted.intValue();
            result.append(c);
        }
        return result.toString();
    }

    public String decryption(String sentence, BigInteger  n, BigInteger  d) {
        StringBuilder decodedBytes = new StringBuilder();
        for (char c : sentence.toCharArray()) {
            BigInteger bi = BigInteger.valueOf(c);
            BigInteger decrypted = bi.modPow(d, n);
            decodedBytes.append((char) decrypted.intValue());
        }
        byte[] bytes = Base64.getDecoder().decode(decodedBytes.toString());
        return new String(bytes);
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
