package dev.jonasbirkeli.WhitelistPurger;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonPrimitive;
import org.bukkit.entity.Player;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;


public class WhitelistUpdater {
    public void updateUsername(Player player) {
        // Provide the UUID and new date string
        String newDateString = LocalDate.now().toString();
        //System.out.println("Player uuid was passed in as " +);
        String playerUuid = player.getUniqueId().toString();
        System.out.println("Got player " + player.getDisplayName());

        // Read the JSON file into a JSON object
        try (FileReader fileReader = new FileReader("./whitelist_dated.json")) {
            JsonParser jsonParser = new JsonParser();
            JsonElement jsonElement = jsonParser.parse(fileReader);

            if (jsonElement.isJsonArray()) {
                JsonArray jsonArray = jsonElement.getAsJsonArray();

                // Iterate through the array to find the matching UUID
                for (JsonElement element : jsonArray) {
                    if (element.isJsonObject()) {
                        JsonObject jsonObject = element.getAsJsonObject();
                        String uuid = jsonObject.get("uuid").getAsString();

                        // Check if the UUID matches
                        if (uuid.equals(playerUuid.replaceAll("[\\s\\-()]", ""))) {
                            // Update the date string
                            player.sendMessage("Oppdaterte siste aktive dato til " + newDateString);
                            jsonObject.add("date", new JsonPrimitive(newDateString));
                        }
                    }
                }

                // Write the updated JSON back to the file
                try (FileWriter fileWriter = new FileWriter("whitelist_dated.json")) {
                    Gson gson = new Gson();
                    gson.toJson(jsonArray, fileWriter);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Fant ikke fil, eller annen feil." + e);
        }
    }
}
