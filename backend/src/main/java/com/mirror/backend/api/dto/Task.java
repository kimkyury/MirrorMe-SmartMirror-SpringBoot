package com.mirror.backend.api.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Task {
    @JsonProperty("kind")
    private String kind;
    @JsonProperty("etag")
    private String etag;
    @JsonProperty("items")
    private List<Task.Item> items;

    public List<Task.Item> getItems() {
        return items;
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Item {
        @JsonProperty("kind")
        private String kind;
        @JsonProperty("id")
        private String id;
        @JsonProperty("etag")
        private String etag;
        @JsonProperty("title")
        private String title;
        @JsonProperty("updated")
        private String updated;
        @JsonProperty("selfLink")
        private String selfLink;
        @JsonProperty("position")
        private String position;
        @JsonProperty("notes")
        private String notes;
        @JsonProperty("status")
        private String status;
        @JsonProperty("due")
        private String due;

        public String getId() {
            return id;
        }
    }
}
