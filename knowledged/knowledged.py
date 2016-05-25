# -*- coding: utf-8-*-
import wolframalpha
from jasper import plugin


class WolframAlphaPlugin(plugin.SpeechHandlerPlugin):
    def get_phrases(self):
        return [self.gettext("WHO"), self.gettext("WHAT"),
                self.gettext("HOW MUCH"), self.gettext("HOW MANY"),
                self.gettext("HOW OLD")]

    def handle(self, text, mic):
        app_id = self.profile['keys']['WOLFRAMALPHA']
        client = wolframalpha.Client(app_id)
        query = client.query(text)
        if len(query.pods) > 0:
            pod = query.pods[1]
            if pod.text:
                texts = pod.text
            else:
                texts = self.gettext("I can not find anything")

            mic.say(texts.replace("|", ""))
        else:
            mic.say(self.gettext("Sorry, Could you be more specific?"))

    def is_valid(self, text):
        return any(p.lower() in text.lower() for p in self.get_phrases())
