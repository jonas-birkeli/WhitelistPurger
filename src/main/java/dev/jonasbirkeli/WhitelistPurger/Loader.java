package dev.jonasbirkeli.WhitelistPurger;

import org.bukkit.entity.Player;


public class Loader extends org.bukkit.plugin.java.JavaPlugin {
    public void onEnable() {
        getServer().getPluginManager().registerEvents(new PlayerJoinListener(), this);
        System.out.println("Whitelist Purger aktiv.");
    }

    // Create a PlayerJoinListener class to handle player join events
    private static class PlayerJoinListener implements org.bukkit.event.Listener {
        WhitelistUpdater whitelistUpdater = new WhitelistUpdater();

        @org.bukkit.event.EventHandler
        public void onPlayerJoin(org.bukkit.event.player.PlayerJoinEvent event) {
            Player player = event.getPlayer();
            whitelistUpdater.updateUsername(player);
        }
    }
}
