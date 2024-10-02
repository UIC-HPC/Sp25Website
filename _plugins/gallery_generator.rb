module Jekyll
	class GalleryPageGenerator < Generator
	  safe true
  
	  def generate(site)
		image_extensions = %w[jpg jpeg png gif]
  
		# Get the path to the images directory
		images_dir = File.join(site.source, 'assets', 'images')
  
		# Check if the images directory exists
		return unless Dir.exist?(images_dir)
  
		# Get the list of gallery names (subdirectories in assets/images)
		galleries = Dir.entries(images_dir).select do |entry|
		  path = File.join(images_dir, entry)
		  File.directory?(path) && !(entry == '.' || entry == '..')
		end
  
		galleries.each do |gallery_name|
		  # Create a new page for the gallery
		  gallery_page = GalleryPage.new(site, site.source, "/gallery/#{gallery_name}/", gallery_name)
		  site.pages << gallery_page
		end
	  end
	end
  
	# Custom Page class for galleries
	class GalleryPage < Page
	  def initialize(site, base, dir, gallery_name)
		@site = site
		@base = base
		@dir  = dir
		@name = 'index.html'
  
		self.process(@name)
		self.read_yaml(File.join(base, '_layouts'), 'gallery_page.html')
		self.data['title'] = gallery_name.capitalize
		self.data['gallery_name'] = gallery_name
		self.data['permalink'] = "/gallery/#{gallery_name}/"
	  end
	end
  end