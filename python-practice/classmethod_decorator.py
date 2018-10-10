# @classmethod parameter

class Blog():
	__tablename__ = 'blog'
	def table_name(self):
		return self.__tablename__
	
	@classmethod
	def table_name(cls):
		return cls.__tablename__

class DerivedBlog(Blog):
	__tablename__ = 'derived_blog'

b = DerivedBlog()
print(b.table_name()) # prints 'derived_blog'