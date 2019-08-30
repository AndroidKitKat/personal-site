module Jekyll
    Jekyll::Hooks.register :site, :post_write do |post|
        cmd = "touch /home/akk/www/personal-site/changed"
        system( cmd )
    end
end
