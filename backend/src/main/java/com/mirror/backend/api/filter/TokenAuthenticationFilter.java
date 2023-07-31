package com.mirror.backend.api.filter;

import org.springframework.http.HttpStatus;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class TokenAuthenticationFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 필터 인스턴스가 생성될 때 호출
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {

        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;

        // Header에서 AccessToken 가져옴
        String accessToken = request.getHeader("access_token");
//        System.out.println("Header에서 꺼냄: " + accessToken);

        // Google Oauth에 AccessToken 유효성 검사 요청
        RestTemplate restTemplate = new RestTemplate();
        StringBuilder googleRequestURL = new StringBuilder();
        googleRequestURL.append("https://www.googleapis.com/oauth2/v1/tokeninfo")
            .append("?access_token=").append(accessToken);

        try {
            restTemplate.getForObject(googleRequestURL.toString(), String.class);
            filterChain.doFilter(servletRequest, servletResponse); // AccessToken이 유효하다면 다음 Filter 또는 Controller로 요청 전달
        } catch (HttpClientErrorException e) {
            if (e.getStatusCode() == HttpStatus.BAD_REQUEST) {
                response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
                response.getWriter().write("Invalid access token"); // AccessToken이 유효하지 않다면 클라이언트에 401 Unauthorized 응답
            } else {
                throw e; // 다른 문제가 발생했다면 예외를 던짐
            }
        }
    }

    @Override
    public void destroy() {

    }
}