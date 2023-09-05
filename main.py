import say_start
import get_maintainers
import get_contributors

say_start.say_begin_words()
name_maintainers,email_maintainers = get_maintainers.maintainers()
name_contributors,email_contributors = get_contributors.contributors()
# 这些都是List类型，不需要转换了
